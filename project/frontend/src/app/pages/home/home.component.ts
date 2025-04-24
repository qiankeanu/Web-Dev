import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {
  constructor(
    private router: Router,
    public authService: AuthService
  ) {}

  navigateToLogin() {
    this.router.navigate(['/login']);
  }

  navigateToRegister() {
    this.router.navigate(['/register']);
  }

  navigateToJobList() {
    this.router.navigate(['/jobs']);
  }

  navigateToSpecialists() {
    this.router.navigate(['/specialists']);
  }

  navigateToCreateVacancy() {
    this.router.navigate(['/create-vacancy']);
  }

  navigateToAiAssistant() {
    this.router.navigate(['/ai-assistant']);
  }

  logout() {
    this.authService.logout();
    this.router.navigate(['/']);
  }
}
