import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-fichas',
  templateUrl: './fichas.page.html',
  styleUrls: ['./fichas.page.scss'],
})
export class FichasPage implements OnInit {
  fichas: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.getFichas();
  }

  getFichas() {
    this.apiService.getFichas().subscribe(data => {
      this.fichas = data;
    });
  }

  alertButtons = ['Voltar'];
}