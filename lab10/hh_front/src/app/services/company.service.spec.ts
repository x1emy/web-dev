import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Company } from '../models';

@Injectable({
  providedIn: 'root'
})
export class CompanyService {
  private apiUrl = 'http://your-api-url.com/companies';  // Укажи правильный URL

  constructor(private http: HttpClient) { }

  getCompanies(): Observable<Company[]> {
    return this.http.get<Company[]>(this.apiUrl);  // Запрос на получение данных
  }
}
