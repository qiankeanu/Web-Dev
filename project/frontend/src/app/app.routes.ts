import { Routes } from '@angular/router';
import { AuthGuard } from './guards/auth.guard';
import { HomeComponent } from './pages/home/home.component';
import { SpecialistListComponent } from './pages/specialist-list/specialist-list.component';
import { JobListComponent } from './pages/job-list/job-list.component';
import { AiAssistantComponent } from './pages/ai-assistant/ai-assistant.component';
import { LoginComponent } from './pages/login/login.component';
import { RegisterComponent } from './pages/register/register.component';
import { CreateVacancyComponent } from './pages/create-vacancy/create-vacancy.component';

export const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'specialists', component: SpecialistListComponent },
  { path: 'jobs', component: JobListComponent },
  { path: 'ai-assistant', component: AiAssistantComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { 
    path: 'create-vacancy', 
    component: CreateVacancyComponent,
    canActivate: [AuthGuard]
  },
  { 
    path: 'ai-assistant', 
    component: AiAssistantComponent,
    canActivate: [AuthGuard]
  },
  { path: '**', redirectTo: '' } // Redirect invalid routes to home
];
