import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Company } from '../company';
import { Router } from '@angular/router';  
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';


@Component({
    selector: 'app-companies',
    templateUrl: './companies.component.html',
    styleUrls: ['./companies.component.css'],
    imports: [CommonModule, RouterOutlet],
    standalone: true  
})
export class CompaniesComponent implements OnInit {

    companies: Company[] = [];

    constructor(private apiService: ApiService, private router: Router) { }  

    ngOnInit(): void {
        this.loadCompanies();
    }

    loadCompanies(): void {
        this.apiService.getCompanies().subscribe(
            (data) => {
                this.companies = data;
            },
            (error) => {
                console.error('Error fetching companies:', error);
            }
        );
    }

    showVacancies(companyId: number): void {
        this.router.navigate(['/company', companyId]);  
    }
}