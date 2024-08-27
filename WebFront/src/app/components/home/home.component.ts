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
  responseMensaje: any;
  mensaje: any;
  mensajeRag: any;
  responseMensajeRag: any;

  isCargandoPostMessage: boolean = false;
  isCargandoPostAgenteRag: boolean = false;


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
    if (this.mensaje) {
      this.isCargandoPostMessage = true;
      console.log("🚀 ~ HomeComponent ~ postMessage ~ this.menssage:", this.mensaje)
      this._flaskService.postMessage(this.mensaje).subscribe({
        next: (res) => {
          this.responseMensaje = res;
          this.isCargandoPostMessage = false;
          console.log("🚀 ~ HomeComponent ~ this._flaskService.postMessage ~ res:", res)
        },
        error: (error: HttpErrorResponse) => {
          console.log(error);
          this.isCargandoPostMessage = false;
        }
      })
    }
  }

  postAgenteRag() {
    if (this.mensajeRag) {
      this.isCargandoPostAgenteRag = true;
      this._flaskService.postAgenteRag(this.mensajeRag).subscribe({
        next: (res: any) => {
          this.responseMensajeRag = res.response;
          this.isCargandoPostAgenteRag = false;
          console.log("🚀 ~ HomeComponent ~ this._flaskService.postMessage ~ res:", res)
        },
        error: (error: HttpErrorResponse) => {
          console.log(error)
          this.isCargandoPostAgenteRag = false;
        }
      })
    }
  }
}
