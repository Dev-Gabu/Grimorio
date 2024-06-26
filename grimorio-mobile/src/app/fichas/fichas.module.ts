import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { IonicModule } from '@ionic/angular';
import { FormsModule } from '@angular/forms';
import { FichasPage } from './fichas.page';

import { FichasPageRoutingModule } from './fichas-routing.module';

import { RouterModule } from '@angular/router';


@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    FichasPageRoutingModule,
    RouterModule.forChild([{ path: '', component: FichasPage }])
  ],
  declarations: [FichasPage],
  exports: [FichasPage]
})
export class FichasPageModule {}
