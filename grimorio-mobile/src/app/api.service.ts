import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, interval } from 'rxjs';
import { switchMap } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private itemUrl = 'http://localhost:8000/item/api/items';
  private fichaUrl = 'http://localhost:8000/fichas/api/fichas';
  private criaturaUrl = 'http://localhost:8000/bestiario/api/criaturas';

  constructor(private http: HttpClient) { }

  getItems(): Observable<any> {
    return this.http.get(this.itemUrl);
  }

  getItemsContinuously(): Observable<any[]> {
    return interval(5000).pipe( // Verifica a cada 5 segundos
      switchMap(() => this.getItems())
    );
  }
  
  getFichas(): Observable<any> {
    return this.http.get(this.fichaUrl);
  }

  getFichasContinuously(): Observable<any[]> {
    return interval(5000).pipe( // Verifica a cada 5 segundos
      switchMap(() => this.getFichas())
    );
  }

  getCriaturas(): Observable<any> {
    return this.http.get(this.criaturaUrl);
  }

  getCriaturasContinuously(): Observable<any[]> {
    return interval(5000).pipe( // Verifica a cada 5 segundos
      switchMap(() => this.getCriaturas())
    );
  }

}
