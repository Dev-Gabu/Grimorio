import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-bestiario',
  templateUrl: './bestiario.page.html',
  styleUrls: ['./bestiario.page.scss'],
})
export class BestiarioPage implements OnInit {
  criaturas: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.getCriaturas();
  }

  getCriaturas() {
    this.apiService.getCriaturas().subscribe(data => {
      this.criaturas = data;
    });
  }

  alertButtons = ['Voltar'];
}
