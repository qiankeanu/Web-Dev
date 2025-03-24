import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import { LaunchFilterComponent } from '../launch-filter/launch-filter.component';

@Component({
  selector: 'app-spacex-launches',
  standalone: true,
  imports: [CommonModule, LaunchFilterComponent],
  templateUrl: './spacex-launches.component.html',
  styleUrl: './spacex-launches.component.css'
})
export class SpacexLaunchesComponent implements OnInit {
  launches: any[] = [];
  filteredLaunches: any[] = [];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get('https://api.spacexdata.com/v5/launches').subscribe((data: any) => {
      this.launches = data;
      this.filteredLaunches = data;
    });
  }

  filterLaunches(successOnly: boolean) {
    this.filteredLaunches = successOnly ?
      this.launches.filter(launch => launch.success)
      : this.launches;
  }
}