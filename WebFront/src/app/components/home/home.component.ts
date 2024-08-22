import { HttpErrorResponse } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';
import { FlaskService } from 'src/app/services/flask.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  newdata: any;
  responseMessage: any;
  menssage: any;

  constructor(private _flaskService: FlaskService) { }

  ngOnInit(): void {
    this.getData();
  }

  getData() {
    this._flaskService.getdata().subscribe({
      next: (res) => {
        this.newdata = res;
      },
      error: (error: HttpErrorResponse) => {
        console.log(error)
      }
    })
  }

  postMessage() {
    //this.menssage = 'Dame la fecha de creacion de EISEI'
    if(this.menssage){
      this._flaskService.postMessage(this.menssage).subscribe({
        next: (res) => {
          this.responseMessage = res;
          console.log("🚀 ~ HomeComponent ~ this._flaskService.postMessage ~ res:", res)
        },
        error: (error: HttpErrorResponse) => {
          console.log(error)
        }
      })
    }
  }
}
