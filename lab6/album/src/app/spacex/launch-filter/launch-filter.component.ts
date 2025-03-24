import { Component, EventEmitter, Output } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-launch-filter',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './launch-filter.component.html',
  styleUrl: './launch-filter.component.css'
})
export class LaunchFilterComponent {
  @Output() filter = new EventEmitter<boolean>();
  isFiltered = false;

  toggleFilter() {
    this.isFiltered = !this.isFiltered;
    this.filter.emit(this.isFiltered);
  }
}