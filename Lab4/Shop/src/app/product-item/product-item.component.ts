import { Component, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent {
  @Input() product: any;
  @Output() liked = new EventEmitter<any>();
  @Output() removed = new EventEmitter<any>();
  @Output() stock = new EventEmitter<any>();
  
  likeProduct() {
    if(this.product.stock > 0){
      this.product.likes++;
      this.product.stock--;
      this.liked.emit(this.product);
    }
  }

  removeProduct() {
    this.removed.emit(this.product);
  }
}
