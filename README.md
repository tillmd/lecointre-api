# Lecointre API

### Description

Return a JSON from [Lecointre menu website](https://32blanche.lecointreparis.com/LP) displaying the menu of the day.

Coded in Python. Can be deployed on Heroku simply by pushing the current code.

### Data

The main input structure is :

```html
<td style="background-image:none;background-color:transparent;" id="tzA2" class="l-0 padding valigntop">
   <div  class="pos20">
      <div  class="pos21">
         <div  class="pos22">
            <table style=" width:247px;height:26px;">
               <tr>
                  <td id="tzA3" class="Normal padding">Menu Du Jour</td>
               </tr>
            </table>
         </div>
      </div>
      <div  class="pos23">
         <div  class="pos24">
            <table style=" width:247px;height:26px;">
               <tr>
                  <td id="tzA14" class="Normal padding">Section</td>
               </tr>
            </table>
         </div>
      </div>
      <div  class="pos25">
         <div  class="pos26">
            <table style=" width:247px;height:26px;">
               <tr>
                  <td id="tzA4" class="Normal padding">Item 1</td>
               </tr>
            </table>
         </div>
      </div>
...
      <div  class="pos47">
         <div  class="pos48">
            <table style=" width:247px;height:26px;">
               <tr>
                  <td id="tzA23" class="Normal padding">Plat Du Chef</td>
               </tr>
            </table>
         </div>
      </div>
      <div  class="pos49">
         <div  class="pos50">
            <table style=" width:247px;height:26px;">
               <tr>
                  <td id="tzA24" class="Normal padding"></td>
               </tr>
            </table>
         </div>
      </div>
...
   </div>
</td>
```

The output structure is :

```json
[
  {
    "name": "Section name",
    "sub": [
      "Item 1",
      "Item 2",
      "..."
    ]
  }
]
```
