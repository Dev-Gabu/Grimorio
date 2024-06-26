import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private itemUrl = 'http://localhost:8000/item/api/items';
  private fichaUrl = 'http://localhost:8000/ficha/api/fichas';
  private criaturaUrl = 'http://localhost:8000/bestiario/api/criaturas';

  constructor(private http: HttpClient) { }

  getItems(): Observable<any> {
    return this.http.get(this.itemUrl);
  }
  
  getFichas(): Observable<any> {
    return this.http.get(this.fichaUrl);
  }

  getCriaturas(): Observable<any> {
    return this.http.get(this.criaturaUrl);
  }

}
