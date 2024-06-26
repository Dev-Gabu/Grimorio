import { ComponentFixture, TestBed } from '@angular/core/testing';
import { BestiarioPage } from './bestiario.page';

describe('BestiarioPage', () => {
  let component: BestiarioPage;
  let fixture: ComponentFixture<BestiarioPage>;

  beforeEach(() => {
    fixture = TestBed.createComponent(BestiarioPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
