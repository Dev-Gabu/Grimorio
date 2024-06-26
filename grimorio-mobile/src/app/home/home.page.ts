import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage implements OnInit {
  items: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit() {
    this.getItems();
  }

  getItems() {
    this.apiService.getItems().subscribe(data => {
      this.items = data;
    });
  }

  alertButtons = ['Voltar'];
  
}
