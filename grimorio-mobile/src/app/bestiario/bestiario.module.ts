import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { IonicModule } from '@ionic/angular';

import { BestiarioPageRoutingModule } from './bestiario-routing.module';

import { BestiarioPage } from './bestiario.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    BestiarioPageRoutingModule,
    RouterModule.forChild([{ path: '', component: BestiarioPage }])
  ],
  declarations: [BestiarioPage],
  exports: [BestiarioPage]
})
export class BestiarioPageModule {}