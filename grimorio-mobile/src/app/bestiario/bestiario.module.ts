import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { BestiarioPageRoutingModule } from './bestiario-routing.module';

import { BestiarioPage } from './bestiario.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    BestiarioPageRoutingModule
  ],
  declarations: [BestiarioPage]
})
export class BestiarioPageModule {}
