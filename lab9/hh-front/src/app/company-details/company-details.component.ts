import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Vacancy } from '../vacancy';
import { ActivatedRoute } from '@angular/router';  
import { CommonModule } from '@angular/common';

@Component({
    selector: 'app-company-details',
    templateUrl: './company-details.component.html',
    styleUrls: ['./company-details.component.css'],
    imports: [CommonModule],
    standalone: true  
    
})
export class CompanyDetailsComponent implements OnInit {

    companyId: number | null = null;
    vacancies: Vacancy[] = [];

    constructor(private apiService: ApiService, private route: ActivatedRoute) { } 

    ngOnInit(): void {
        this.route.paramMap.subscribe(params => {   
            const id = params.get('id');
            this.companyId = id ? +id : null; 
            if (this.companyId !== null) {
                this.loadVacancies();
            }
        });
    }

    loadVacancies(): void {
        if (this.companyId !== null) {
            this.apiService.getCompanyVacancies(this.companyId).subscribe(
                (data) => {
                    this.vacancies = data;
                },
                (error) => {
                    console.error('Error fetching vacancies:', error);
                }
            );
        }
    }
}