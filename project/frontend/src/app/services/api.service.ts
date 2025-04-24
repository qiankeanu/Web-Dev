import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';
import {
  ChatResponse,
  VacancyData,
  AuthResponse,
  Profile,
  RegisterData,
  LoginCredentials
} from '../types/api.types';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://localhost:8000';

  constructor(private http: HttpClient) {}

  // Auth endpoints
  

  login(credentials: {email: string, password: string}): Observable<AuthResponse> {
    return this.http.post<AuthResponse>(`${this.baseUrl}/token/`, {
      username: credentials.email,  // Send email as username
      password: credentials.password
    });
  }

//   login(email: string, password: string): Observable<any> {
//     return this.http.post(`${this.baseUrl}/token/`, { email, password });
//   }

  register(userData: RegisterData): Observable<any> {
    const formData = new FormData();
    formData.append('username', userData.username);
    formData.append('email', userData.email);
    formData.append('password', userData.password);
    
    // Add profile data
    const profileData = userData.profile;
    Object.entries(profileData).forEach(([key, value]) => {
      if (value !== null && value !== undefined) {
        formData.append(`profile.${key}`, value);
      }
    });

    return this.http.post(`${this.baseUrl}/users/register/`, formData);
  }

  // Profile endpoints
  getProfile(id: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/users/profile/${id}/`);
  }

  // Profile methods
  updateProfile(profileId: number, data: Partial<Profile>): Observable<Profile> {
    return this.http.put<Profile>(`${this.baseUrl}/users/profile/${profileId}/`, data);
  }

  uploadResume(profileId: number, file: File): Observable<any> {
    const formData = new FormData();
    formData.append('resume_file', file);
    formData.append('profile_id', profileId.toString());
    return this.http.post(`${this.baseUrl}/ai/parse-resume/`, formData);
  }

  // Skills endpoints
  getSkills(): Observable<any> {
    return this.http.get(`${this.baseUrl}/skills/skills/`);
  }

  getSpecialists(skills: string[] = []): Observable<any> {
    let params = new HttpParams();
    if (skills.length > 0) {
      params = params.set('skills', skills.join(','));
    }
    return this.http.get(`${this.baseUrl}/users/specialists/`, { params });
  }

  getMatchingProfiles(profileId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/ai/match-profiles/${profileId}/`);
  }

  // Chat endpoints
  sendChatMessage(message: string): Observable<ChatResponse> {
    return this.http.post<ChatResponse>(`${this.baseUrl}/ai/chat/`, { message });
  }

  // Vacancy endpoints
  createVacancy(vacancy: VacancyData): Observable<any> {
    return this.http.post(`${this.baseUrl}/vacancies/create/`, vacancy);
  }

  getVacancies(): Observable<any> {
    return this.http.get(`${this.baseUrl}/vacancies/`);
  }

  searchVacancies(query: string): Observable<any> {
    const params = new HttpParams().set('q', query);
    return this.http.get(`${this.baseUrl}/vacancies/search/`, { params });
  }

  // Skills methods
  addUserSkill(profileId: number, skillId: number): Observable<any> {
    return this.http.post(`${this.baseUrl}/skills/user-skills/`, {
      user: profileId,
      skill: skillId
    });
  }

  getUserSkills(profileId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/skills/user-skills/${profileId}/`);
  }

  // Token refresh
  refreshToken(refresh: string): Observable<AuthResponse> {
    return this.http.post<AuthResponse>(`${this.baseUrl}/token/refresh/`, { refresh });
  }
}