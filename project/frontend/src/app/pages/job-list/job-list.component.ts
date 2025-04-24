import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms'; 

@Component({
  selector: 'app-job-list',
  standalone: true,
  imports: [CommonModule, FormsModule], 
  templateUrl: './job-list.component.html',
  styleUrls: ['./job-list.component.scss'],
})
export class JobListComponent {
  jobs = [
    { title: 'Frontend Developer', company: 'Company A' },
    { title: 'Backend Developer', company: 'Company B' },
    { title: 'Fullstack Developer', company: 'Company C' },
  ];
}
