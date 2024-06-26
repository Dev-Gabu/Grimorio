import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

import { TabBarComponent } from './tab-bar/tab-bar.component'

const routes: Routes = [
  {
    path: '',
  component: TabBarComponent,
  children: [
    {
      path: 'home',
      loadChildren: () => import('./home/home.module').then( m => m.HomePageModule)
    },
    {
      path: '',
      redirectTo: 'home',
      pathMatch: 'full'
    },
    {
      path: 'fichas',
      loadChildren: () => import('./fichas/fichas.module').then( m => m.FichasPageModule)
    },
    {
      path: 'bestiario',
      loadChildren: () => import('./bestiario/bestiario.module').then( m => m.BestiarioPageModule)
    },
  ],
  },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
