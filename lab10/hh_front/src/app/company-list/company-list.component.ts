import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { CompanyService } from '../services/company.service';
import { Company,Vacancy } from '../models';
import { CompanyVacanciesComponent } from '../company-vacancies/company-vacancies.component';

@Component({
  selector: 'app-company-list',
  standalone: true,
  imports: [CommonModule, CompanyVacanciesComponent],
  providers: [CompanyService],
  templateUrl: './company-list.component.html',
  styleUrls: ['./company-list.component.css']
})
export class CompanyListComponent implements OnInit {
  companies: Company[] = [];
  selectedCompanyId: number | null = null;

  constructor(private companyService: CompanyService) {}

  ngOnInit(): void {
    this.companyService.getCompanies().subscribe((data) => {
      this.companies = data;
    });
  }

  onSelectCompany(id: number): void {
    this.selectedCompanyId = id;
  }
}
