import { Routes } from '@angular/router';
import { CompaniesComponent } from './companies/companies.component';
import { CompanyDetailsComponent } from './company-details/company-details.component';

export const routes: Routes = [
    { path: 'companies', component: CompaniesComponent },
    { path: 'company/:id', component: CompanyDetailsComponent }, 
    { path: '', redirectTo: '/companies', pathMatch: 'full' },  
];