import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router, RouterModule } from '@angular/router';
import { ApiService } from '../../services/api.service';
import { AuthService } from '../../services/auth.service';
import { RegisterData, ProfileData } from '../../types/api.types';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterModule],
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
})
export class RegisterComponent {
  // Basic user data
  username: string = '';
  email: string = '';
  password: string = '';
  confirmPassword: string = '';
  
  // Profile data
  surname: string = '';
  middleName: string = '';
  givenName: string = '';
  birthday: string = '';
  phoneNumber: string = '';
  status: string = 'AS'; // Default to Active Searching
  photo: File | null = null;
  
  error: string = '';

  statusOptions = [
    { value: 'AS', label: 'Actively Searching' },
    { value: 'S', label: 'Currently Employed, Searching' },
    { value: 'NR', label: 'Currently Employed, Open to Offers' },
    { value: 'NI', label: 'Not Interested in Offers' }
  ];

  constructor(
    private apiService: ApiService,
    private authService: AuthService,
    private router: Router
  ) {}

  onPhotoSelected(event: any) {
    const file = event.target.files[0];
    if (file) {
      this.photo = file;
    }
  }

  register() {
    if (this.password !== this.confirmPassword) {
      this.error = 'Passwords do not match';
      return;
    }

    const registerData: RegisterData = {
      username: this.username,
      email: this.email,
      password: this.password,
      profile: {
        surname: this.surname,
        middle_name: this.middleName,
        given_name: this.givenName,
        birthday: this.birthday,
        phone_number: this.phoneNumber,
        status: this.status,
        ...(this.photo && { photo: this.photo })
      }
    };

    this.apiService.register(registerData).subscribe({
      next: (response) => {
        this.apiService.login({
          email: this.email,  // Use email instead of username
          password: this.password
        }).subscribe({
          next: (loginResponse) => {
            localStorage.setItem('token', loginResponse.access);
            this.apiService.getProfile(loginResponse.user_id).subscribe(user => {
              this.authService.setUser(user);
              this.router.navigate(['/']);
            });
          }
        });
      },
      error: (error) => {
        this.error = error.error?.detail || 'Registration failed';
      }
    });
  }
}
