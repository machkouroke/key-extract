Key Term Extraction
============

### Extract the important term in a text
![image](https://user-images.githubusercontent.com/40785379/180315389-a894663f-9bed-4d6f-b26f-9a8799677b9c.png)
<a href="https://buymeacoffee.com/machkouroke" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: auto !important;width: auto !important;" ></a>


## How use Key Term Extraction ?
You just have to fill your text in an xml file with a structure similar to the news.xml file and then enter the file path
```xml
<?xml version='1.0' encoding='UTF8'?>
<data>
  <corpus>
    <news>
      <value name="head">Title</value>
      <value name="text">
        <!-- Text -->
      </value>
    </news>
    <!-- And so on -->
  </corpus>
</data>
```
