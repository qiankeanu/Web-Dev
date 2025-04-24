import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ApiService } from '../../services/api.service';

@Component({
  selector: 'app-specialist-list',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './specialist-list.component.html'
})
export class SpecialistListComponent implements OnInit {
  specialists: any[] = [];
  skills: any[] = [];
  selectedSkills: string[] = [];
  searchQuery: string = '';

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.loadSkills();
    this.loadSpecialists();
  }

  loadSkills() {
    this.apiService.getSkills().subscribe({
      next: (response) => {
        this.skills = response;
      },
      error: (error) => console.error('Error loading skills:', error)
    });
  }

  loadSpecialists() {
    this.apiService.getSpecialists(this.selectedSkills).subscribe({
      next: (response) => {
        this.specialists = response;
      },
      error: (error) => console.error('Error loading specialists:', error)
    });
  }

  toggleSkill(skill: string) {
    const index = this.selectedSkills.indexOf(skill);
    if (index === -1) {
      this.selectedSkills.push(skill);
    } else {
      this.selectedSkills.splice(index, 1);
    }
    this.loadSpecialists();
  }

  searchSpecialists() {
    this.loadSpecialists();
  }
}