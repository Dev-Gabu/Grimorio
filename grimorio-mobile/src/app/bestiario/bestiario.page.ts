import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-bestiario',
  templateUrl: './bestiario.page.html',
  styleUrls: ['./bestiario.page.scss'],
})
export class BestiarioPage implements OnInit {
  criaturas: any[] = [];
  private criaturasSubscription: Subscription = new Subscription;

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.getCriaturas();
  }

  getCriaturas() {
    this.apiService.getCriaturas().subscribe(data => {
      this.criaturas = data;
    });
  }

  getCriaturasContinuously() {
    this.criaturasSubscription = this.apiService.getCriaturasContinuously().subscribe(data => {
      this.criaturas = data;
    });
  }

  ngOnDestroy() {
    // Cancelar a subscrição quando o componente for destruído
    if (this.criaturasSubscription) {
      this.criaturasSubscription.unsubscribe();
    }
  }

  alertButtons = ['Voltar'];
}
