import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';
import { routes } from './app/app.routes';  // Changed from appRoutes to routes

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));
