export interface ChatResponse {
  message: string;
}

export interface VacancyData {
  title: string;
  company: string;
  description: string;
  requirements: string;
  salary_range: string;
  location: string;
  employment_type: string;
  experience_level: string;
}

export interface AuthResponse {
  access: string;
  refresh: string;
  user_id: number;
}

export interface Profile {
  id: number;
  user: number;
  skills: any[];
  experience: string;
  education: string;
}

export interface ProfileData {
  surname: string;
  middle_name: string;
  given_name: string;
  birthday: string;
  phone_number: string;
  status: string;
  photo?: File;
}

export interface RegisterData {
  username: string;
  email: string;
  password: string;
  profile: ProfileData;
}

export interface LoginCredentials {
  email: string;
  password: string;
}