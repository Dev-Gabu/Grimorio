import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-fichas',
  templateUrl: './fichas.page.html',
  styleUrls: ['./fichas.page.scss'],
})
export class FichasPage implements OnInit {
  fichas: any[] = [];
  private fichasSubscription: Subscription = new Subscription;

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.getFichas();
  }

  getFichas() {
    this.apiService.getFichas().subscribe(data => {
      this.fichas = data;
    });
  }

  getFichasContinuously() {
    this.fichasSubscription = this.apiService.getFichasContinuously().subscribe(data => {
      this.fichas = data;
    });
  }

  ngOnDestroy() {
    // Cancelar a subscrição quando o componente for destruído
    if (this.fichasSubscription) {
      this.fichasSubscription.unsubscribe();
    }
  }

  alertButtons = ['Voltar'];
}