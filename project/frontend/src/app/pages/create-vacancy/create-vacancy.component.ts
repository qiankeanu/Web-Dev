import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-create-vacancy',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './create-vacancy.component.html',
  styleUrls: [] // Remove reference to non-existent scss file
})
export class CreateVacancyComponent {
  vacancy = {
    title: '',
    company: '',
    description: '',
    requirements: '',
    salary_range: '',
    location: '',
    employment_type: 'FULL_TIME',
    experience_level: 'ENTRY'
  };

  constructor(
    private apiService: ApiService,
    public router: Router  // Changed from private to public
  ) {}

  createVacancy() {
    this.apiService.createVacancy(this.vacancy).subscribe({
      next: (response) => {
        console.log('Vacancy created successfully', response);
        this.router.navigate(['/']);
      },
      error: (error) => {
        console.error('Error creating vacancy', error);
      }
    });
  }
}