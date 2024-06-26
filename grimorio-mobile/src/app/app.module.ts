import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClient, HttpClientModule } from '@angular/common/http';

import { IonicModule } from '@ionic/angular';

import { TabBarComponent } from './tab-bar/tab-bar.component';
import { AppComponent } from './app.component';

import { AppRoutingModule } from './app-routing.module';

@NgModule({
  imports: [BrowserModule, FormsModule, AppRoutingModule, IonicModule.forRoot(),HttpClientModule],
  declarations: [AppComponent,TabBarComponent],
  bootstrap: [AppComponent],
})
export class AppModule {}