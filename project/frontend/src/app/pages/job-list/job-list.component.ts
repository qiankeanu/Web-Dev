import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-job-list',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './job-list.component.html',
  styleUrls: ['./job-list.component.scss']
})
export class JobListComponent implements OnInit {
  searchQuery: string = '';
  vacancies: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.loadVacancies();
  }

  loadVacancies() {
    this.apiService.getVacancies().subscribe({
      next: (response) => {
        this.vacancies = response;
      },
      error: (error) => {
        console.error('Error loading vacancies:', error);
      }
    });
  }

  searchVacancies() {
    this.apiService.searchVacancies(this.searchQuery).subscribe({
      next: (response) => {
        this.vacancies = response;
      },
      error: (error) => {
        console.error('Error searching vacancies:', error);
      }
    });
  }
}
