import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SpacexLaunchesComponent } from './SpacexLaunchesComponent';

describe('SpacexLaunchesComponent', () => {
  let component: SpacexLaunchesComponent;
  let fixture: ComponentFixture<SpacexLaunchesComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SpacexLaunchesComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SpacexLaunchesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
