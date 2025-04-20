import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Company } from './company';
import { Vacancy } from './vacancy';

@Injectable({
    providedIn: 'root'
})
export class ApiService {

    private baseUrl = 'http://127.0.0.1:8000/api' ;  

    constructor(private http: HttpClient) { }

    getCompanies(): Observable<Company[]> {
        return this.http.get<Company[]>(`${this.baseUrl}/companies/`);
    }

    getCompanyVacancies(companyId: number): Observable<Vacancy[]> {
        return this.http.get<Vacancy[]>(`${this.baseUrl}/companies/${companyId}/vacancies/`);
    }

    getVacancies(): Observable<Vacancy[]> {
     return this.http.get<Vacancy[]>(`${this.baseUrl}/vacancies/`);
    }
}