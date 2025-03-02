import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent {
  @Input() products: any[] = [];
  @Output() liked = new EventEmitter<any>();
  @Output() removed = new EventEmitter<any>();

  likeProduct(product: any) {
    this.liked.emit(product); 
  }

  removeProduct(product: any) {
    this.removed.emit(product); 
  }
}
