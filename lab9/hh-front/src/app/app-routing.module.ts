import { Routes } from '@angular/router';
import { VacanciesListComponent } from './vacancies-list/vacancies-list.component';
import { CompaniesListComponent } from './companies-list/companies-list.component';

const routes: Routes = [
    { path: '', component: CompaniesListComponent },
    { path: 'companies/:id/vacancies', component: VacanciesListComponent }
];