import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";

@Injectable({
    providedIn: 'root'
})

export class FlaskService {

    constructor(private _http: HttpClient) { }

    getdata() {
        return this._http.get('http://127.0.0.1:5000/api/data');
    }

    postMessage(message: string) {
        const formData = new FormData();
        formData.append("message", message);
        return this._http.post('http://127.0.0.1:5000/api/message', formData);
      }
}
