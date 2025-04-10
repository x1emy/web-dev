import { Component, Input, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { VacancyService } from '../services/vacancy.service';  // Импортируй сервис
import { Vacancy } from '../models';

@Component({
  selector: 'app-company-vacancies',
  standalone: true,
  imports: [CommonModule],
  providers: [VacancyService],  // Указываем сервис в providers
  templateUrl: './company-vacancies.component.html',
  styleUrls: ['./company-vacancies.component.css']
})
export class CompanyVacanciesComponent implements OnInit {
  @Input() companyId: number | null = null;
  vacancies: Vacancy[] = [];

  constructor(private vacancyService: VacancyService) { }

  ngOnInit(): void {
    if (this.companyId) {
      this.vacancyService.getVacanciesByCompany(this.companyId).subscribe((data: Vacancy[]) => {
        this.vacancies = data;
      });
    }
  }
}
