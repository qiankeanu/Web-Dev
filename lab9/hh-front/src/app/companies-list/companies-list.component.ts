import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Company } from '../company';

@Component({
  selector: 'app-companies-list',
  templateUrl: './companies-list.component.html',
  styleUrls: ['./companies-list.component.css']
})
export class CompaniesListComponent implements OnInit {
  companies: Company[] = [];

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
    this.apiService.getCompanies().subscribe(data => {
      this.companies = data;
    });
  }
}