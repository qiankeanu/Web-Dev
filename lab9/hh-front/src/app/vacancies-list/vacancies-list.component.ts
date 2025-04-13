import { Component, Input, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Vacancy } from '../vacancy';

@Component({
  selector: 'app-vacancies-list',
  templateUrl: './vacancies-list.component.html',
  styleUrls: ['./vacancies-list.component.css']
})
export class VacanciesListComponent implements OnInit {
  @Input() companyId!: number;
  vacancies: Vacancy[] = [];

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.apiService.getVacancies(this.companyId).subscribe(data => {
      this.vacancies = data;
    });
  }
}