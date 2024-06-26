import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { BestiarioPage } from './bestiario.page';

const routes: Routes = [
  {
    path: '',
    component: BestiarioPage
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class BestiarioPageRoutingModule {}
