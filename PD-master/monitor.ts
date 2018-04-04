import { Component,  ViewChild  } from '@angular/core';
import { NavController} from 'ionic-angular';
import { AngularFireDatabase } from 'angularfire2/database';
import { Chart } from 'chart.js';

@Component({
  selector: 'page-monitor',
  templateUrl: 'monitor.html'
})

export class MonitorPage {
  timeStamp = []
  valueTemp = []
  dates = []
  result =[]
  sensor_humidity = ""
  sensor_acidity = ""
  sensor_temperature = ""
  humidity = ""
  acidity = ""
  temperature = ""
  cropName1 = ""
  cropName2 = ""
  cropName3 = ""
  
  @ViewChild('lineCanvas') lineCanvas;
  
  lineChart: any;

  arrData: any;
  arrName: any;
  
  constructor(public navCtrl: NavController, public firebaseDb: AngularFireDatabase){
	
    this.firebaseDb.list('/Sensor_Data').valueChanges().subscribe(snapshots=>{
        this.arrData = snapshots;
		
        this.sensor_humidity = this.arrData[0];
        this.sensor_acidity = this.arrData[1];
        this.sensor_temperature = this.arrData[2];
        this.humidity = this.arrData[3];
        this.acidity = this.arrData[4];
        this.temperature = this.arrData[5];

    });
	this.firebaseDb.list('/Crop_Data/Crop_Name').valueChanges().subscribe(snapshots=>{
        this.arrName = snapshots;
		
        this.cropName1 = this.arrName[0];
        this.cropName2 = this.arrName[1];
        this.cropName3 = this.arrName[2];


    });
    var datem = "";
    var year = "";
    var month = "";
    var day = "";
    this.firebaseDb.list('Realtime_Data', ref => ref.limitToLast(1)).snapshotChanges().map(actions =>{
      return actions.map(action => ({ key: action.key, ...action.payload.val()}));
    }).subscribe(dates => {
      dates.map(date => {
        year = date.key;
        console.log(year);
        this.firebaseDb.list('Realtime_Data/'+year, ref => ref.limitToLast(1)).snapshotChanges().map(actions =>{
          return actions.map(action => ({ key: action.key, ...action.payload.val()}));
        }).subscribe(dates => {
          dates.map(date => {
            month = date.key;
            console.log(month);
            this.firebaseDb.list('Realtime_Data/'+year+'/'+month, ref => ref.limitToLast(1)).snapshotChanges().map(actions =>{
              return actions.map(action => ({ key: action.key, ...action.payload.val()}));
            }).subscribe(dates => {
              dates.map(date => {
                day = date.key;
                console.log(day);
                this.firebaseDb.list('Realtime_Data/'+year+'/'+month+'/'+day, ref => ref.limitToLast(1)).snapshotChanges().map(actions =>{
                  return actions.map(action => ({ key: action.key, ...action.payload.val()}));
                }).subscribe(dates => {
                  dates.map(date => {
                    datem = date.key;
                    console.log(datem);

                    this.firebaseDb.list('Realtime_Data/'+year+'/'+month+'/'+day+'/'+datem, ref => ref.limitToLast(1)).valueChanges().subscribe(snapshots=>{
                      this.dates = [];
                      this.result = snapshots;
                      this.result.map(key => {
                        this.dates.push(key.Date_Complete);
                      });
                    });
                    this.firebaseDb.list('Realtime_Data/'+year+'/'+month+'/'+day+'/'+datem, ref => ref.limitToLast(10)).valueChanges().subscribe(snapshots=>{
                      this.valueTemp = [];
                      this.timeStamp = [];
                      this.result = snapshots;
                      this.result.map(key => {
                        this.valueTemp.push(key.Measured_Temp_C);
                        this.timeStamp.push(key.Time);
                      });
                    });

                  }); 
                });
              });
            });
          });
        });
      });
    });


    console.log(this.valueTemp);
    //var getValueTemp = [];
    /*
    this.firebaseDb.list('Realtime_Data', ref => ref.limitToLast(12)).valueChanges().subscribe(snapshots=>{
      this.result = snapshots;
      this.result.map(key => {
        this.valueTemp.push(key.Measured_Temp_C);
      });
    });
	*/
	/*
    this.firebaseDb.list("/Sensor_Data", { preserveSnapshot: true})
    .subscribe(snapshots=>{
        snapshots.forEach(snapshot => {
            if(snapshot.key=="Optimal_Humidity"){
              this.humidity = snapshot.val();
            }
            if(snapshot.key=="Optimal_Temperature"){
              this.temperature = snapshot.val();
            }
            if(snapshot.key=="Optimal_PhLevel"){
              this.acidity = snapshot.val();
            }
            if(snapshot.key=="Measured_Humidity"){
              this.sensor_humidity = snapshot.val();
            }
            if(snapshot.key=="Measured_Temperature"){
              this.sensor_temperature = snapshot.val();
            } 
            if(snapshot.key=="Measured_PhLevel"){
              this.sensor_acidity = snapshot.val();
            } 
        });
    } );*/
  }


  ionViewDidLoad(){
    console.log(this.dates);
    var temp = this;
    setInterval(function(){
      temp.lineChart = new Chart(temp.lineCanvas.nativeElement, {
      type: 'line',
      data: {
        labels: temp.timeStamp,
        datasets: [{
          label: temp.dates,
          backgroundColor: 'rgba(77,83,96,0.2)',
          borderColor: 'rgba(77,83,96,1)',
          pointBackgroundColor: 'rgba(77,83,96,1)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(77,83,96,1)',
          data: temp.valueTemp,
          spanGaps: false,
        }]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        scales: {
          yAxes: [{
            ticks: {
              beginAtZero: false,
              max: 30,
              min: 0
            }
          }] 
        }
        
      }
    
    });

      temp.lineChart.update();
    }, 5000);
  }


}

