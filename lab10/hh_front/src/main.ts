import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app/app.component';
import { provideHttpClient } from '@angular/common/http';
import { appConfig } from './app/app.config'; // импортируешь конфигурацию

// Прямо используем bootstrapApplication для инициализации приложения
bootstrapApplication(AppComponent, {
  providers: [
    provideHttpClient(), // провайдер для работы с HTTP
    // Добавьте дополнительные провайдеры здесь, если необходимо
  ]
}).catch(err => console.error(err));
