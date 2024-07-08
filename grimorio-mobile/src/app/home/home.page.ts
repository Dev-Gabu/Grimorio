import { Component, OnInit, OnDestroy } from '@angular/core';
import { ApiService } from '../api.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit, OnDestroy {
  items: any[] = [];
  private itemsSubscription: Subscription = new Subscription;

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.getItemsContinuously();
  }

  getItemsContinuously() {
    this.itemsSubscription = this.apiService.getItemsContinuously().subscribe(data => {
      this.items = data;
    });
  }

  ngOnDestroy() {
    // Cancelar a subscrição quando o componente for destruído
    if (this.itemsSubscription) {
      this.itemsSubscription.unsubscribe();
    }
  }

  alertButtons = ['Voltar'];
}
