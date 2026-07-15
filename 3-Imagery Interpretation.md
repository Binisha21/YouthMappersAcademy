---
title: "Imagery Interpretation"
author: "YouthMappers Academy"
date: "2024"
update: "2026"
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5

---

# Image Interpretation
This is the third of six courses that make up the Introduction to Mapping with YouthMappers learning track.

## Overview 
Welcome to Module 3 of the YouthMappers Academy. In this course, you will learn about the sources of imagery for tracing in OSM and how to interpret the images you see. Image interpretation is the act of identifying objects within an image and determining their significance. The more familiar you are with the area, the easier this is for you to do, generally. This is why we suggest you start by mapping in an area that you know until you become accustomed to how familiar features look from aerial imagery.

### In this course, you will learn about:
- Natural Color Composite Imagery, the most commonly used imagery type for tracing features in OSM
- The different applications of raster and vector data (images versus traced map features)
- Tips and clues on how to recognize features from imagery


## An Introduction to Imagery Interpretation for OSM

### The Role of Imagery in the OSM Workflow
Tracing features from satellite imagery is one of the most common ways in which mappers contribute to OpenStreetMap. Imagery allows remote mappers to contribute to global tasks when a crisis arises, and even allows locally-based field mappers to “lay the groundwork” so to speak, before organizing fieldwork campaigns to collect specific, detailed tags.

![alt text](https://github.com/Binisha21/YouthMappersAcademy/blob/Patch/Course_Updates/Module3_Static/3.2%20Image%20interpretation.webp)
Figure: A sample of aerial imagery tiles showing the diversity of land cover and land use types a mapper may encounter in OpenStreetMap.
*Source: Frontiers | Automated road surface classification in OpenStreetMap*

```{admonition} Watch This!
Did you ever wonder how your camera actually takes a picture? It's all about light - it records the light that objects reflect. This video explores the basic principles used by optical sensors like Landsat, AVIRIS, and other remote sensing sensors to record the things that we can't see with our eyes. It explains the basic principles of the electromagnetic spectrum, bands and spectral resolution in data and the uses of spectral data to answer science questions.

**Watch The Video**: [Mapping the Invisible: Introduction to Spectral Remote Sensing](https://www.youtube.com/watch?v=3iaFzafWJQE&t=22s)
```

### Two Types of Geospatial Data: Raster and Vector
Before diving into imagery interpretation, it helps to understand the two fundamental types of geospatial data you will encounter in OpenStreetMap — because everything in this course is about the relationship between them.

#### Raster Data
Raster data represents the world as a **grid of cells (pixels)**. Each pixel stores a single value — typically a measure of color or brightness. Think of it exactly like a digital photograph: zoom in far enough and you will see individual squares of color. Satellite imagery is raster data.

![alt text](Module3_Static/3.2.png)
Figure: From real-life to a raster depiction 
*Source: NEON (The National Ecological Observatory Network)*

Raster data is rich in visual detail but carries **no inherent meaning** on its own. A pixel only knows its color. It cannot tell you whether you are looking at a school, a road, or a river — that interpretation is entirely up to you.

#### Vector Data
Vector data represents the world using **points, lines, and polygons** — each with attributes (tags) that describe what that feature actually is. Unlike a pixel, a tagged vector feature carries **meaning**. A polygon becomes a hospital. A line becomes a highway. A point becomes a water pump.

![alt text](https://github.com/Binisha21/YouthMappersAcademy/blob/Patch/Course_Updates/Module3_Static/3.2%20vector)
Figure: Vector data uses points, lines, and polygons to represent discrete geographic features.
*Source: UConn Library: Geographic Information Systems (GIS) — Spatial Data Models*

#### From Raster to Vector — What We Do in OSM

When you trace a building outline in iD Editor, you are doing exactly this: converting raster information (a satellite image) into vector data (a tagged polygon in OSM). This 
conversion — from pixel to feature — is what imagery interpretation is all about.

### An Introduction to Imagery Interpretation

Most of the imagery available to us in OpenStreetMap is called Natural Color Composite Imagery, which corresponds to how we usually see the world. Vegetation appears in various shades of green, water can be anything from bright blue to black, and bare earth and impervious surfaces are light gray and brown. To create this imagery, sensors capture the amount of sunlight (typically in the Blue, Green, and Red wavelengths) reflected off the Earth’s surface. Because different objects reflect light differently, this allows us to identify or perceive these different objects by their relative “color”.

If you are interested in the science behind sensors, and how they capture imagery, please take a closer look [here](https://www.earthdata.nasa.gov/learn/earth-observation-data-basics/remote-sensing).

![alt text](Module3_Static/3.1.png)
*Source: National Ecological Observatory Network (NEON)*

The images we use are stored in digital format by subdividing the entire image area into small equal-sized and similarly shaped areas called pixels. Each pixel represents the brightness of each area with a numeric value or digital number. Data stored in this format is called raster data.

When we zoom back out we can see how individual pixels create features in the image. The key is to study the image for these recognizable features and turn them into points, lines, and areas (polygons) in OSM. This workflow involves identifying and evaluating individual objects and marking their locations by dropping a point or drawing along a linear feature to create a line, or, by tracing around the perimeter of an object to create an area (or polygon).

```{admonition} Bonus Reading Material!
To someone wanting to learn more about remote sensing, this [NASA ARSET Fundamentals of Remote Sensing course](https://www.earthdata.nasa.gov/learn/trainings/fundamentals-remote-sensing) is a free, self-paced course covering how satellites and sensors work.
```

### Advantages of Vector Data

**Why do we trace shapes from imagery, rather than use the wonderfully detailed images already at our disposal?**

Unprocessed satellite imagery has very few practical applications. It is limited by the fact that objects appearing in an image are identifiable by virtue of viewer interpretation. There is very little meaning or context to these objects outside of what the viewer can determine. 

For instance:
- You can’t search satellite images for the nearest pharmacy.
- You can’t generate travel directions from satellite images.

We tend to prefer vector data (point, line, or area data with labels, tags, and attributes) over raw imagery for certain types of analysis because:

- Vector data is easier to organize and query. Because it’s labeled or tagged, we can select it by type using real language queries. 
- Some analysis techniques need the data to be in point/line/polygon format, as a “pixel” with a “reflectance value” doesn’t mean anything within the context of the analysis.
- Our interpretation of imagery is subjective but powerful⏤we appreciate the subtle differences in what constitutes a “school”⏤in the way a computer can’t.

While we are making strides using machine learning to help us scour imagery and detect specific features, it’s still a progressing science, and, as yet, it cannot match the level of contextual detail that human interpretation provides.

![alt text](Module3_Static/3.3.png)

*Source: iD Editor Tutorial*

Looking at the example above, we can see how we represent complex objects, like a parking lot, using more simple features:

a) an area (polygon shape) representing the full extent of the parking area, and 
b) lines representing the paths along which cars navigate the space.   

Although seemingly simple, there are quite a few nuances. For instance, note that the parking lot lines end by connecting to the road centerline; this is so that there is “connectivity” between the road and the parking lot. Without that connection, navigation software will not understand that cars can turn into the parking lot from the adjacent road. It’s the human interpretation of the image and the correct recording of that interpretation in the database that provides us the critical information we need to model and analyze using the type of vector data that OSM contains.

## Sources of Imagery for OSM
Imagery used for tracing within OSM is acquired directly overhead; this is called a vertical perspective, which provides a top-down view of the area of interest. Imagery within OSM can be obtained from numerous sources including satellites, drones, and airborne sensors. We use these data because they can cover large areas very quickly at very high spatial resolutions. Because of the very high spatial resolution, a large number of pixels make up an object which allows you to visually identify individual objects within the image. 

Global high-resolution imagery is available from a handful of providers (which generously donate access to OSM). These include [Bing](https://wiki.openstreetmap.org/wiki/Bing_Maps), [ESRI](https://www.esri.com/en-us/home), [Mapbox](https://www.mapbox.com/), and [Maxar (now Vantor)](https://vantor.com). In many cases, we can take advantage of multiple sets of imagery to help us delineate objects on the ground. 

For instance, in the bottom example below, we see how Bing and Maxar data can provide meaningful differences that can help us distinguish objects. One critical factor here is shadow. Since these images were taken at different times, we can exploit those differences to help us identify individual buildings. Also, if you look at the bottom image below, the four cars parked in one of the gaps in the buildings gives one a sense of scale and an idea that roads connect to this area.

*Bing:*
![alt text](Module3_Static/3.4.png)

*Maxar:*
![alt text](Module3_Static/3.5.png)


## Recognizing Features or Objects from Imagery
The key to the proper use of imagery in OSM is understanding how to appropriately translate what you are seeing on the image, using the tools provided, to create points, lines, areas, and related tags. 

Here is some basic advice to help you decide:
 
![alt text](Module3_Static/ym3.2.png)

In order to identify objects, we need to look for clues in the imagery. See below to learn more: 

- **Determine the size/scale of the area**  
  If you’re working within a platform that provides a scale bar (like [OSM](https://www.openstreetmap.org/)), then you’re already at an advantage. You can use this to roughly determine the dimensions of property areas and built infrastructure.

- **Look for patterns, shapes, and textures**  
  Patterns, shapes, and textures provide critical clues. For instance,roofs will tend to be rectangular, smooth, or wavy (if corrugated). A plot of crops will be an irregular polygon, and have complex texture.

- **Define the colors**
Including tones, and shadows. 

- **Consider your prior knowledge**  
  Prior knowledge can be extremely helpful in interpreting an image. For instance, identifying a thatch hut can be difficult if you have never seen one. 
  
  Sometimes it's helpful to take a tour of the area of interest in [Google Street View](https://www.google.com/maps) or [Flickr World Photos](https://www.flickr.com/map).

- **Association**  
  Notice the relationship between the object you are classifying and recognizable objects or features. For instance, commercial warehouses will tend to be located very close to paved roads.

### Let's Think About Buildings
Let’s practice and pretend that we are trying to find building footprints in OSM:

- **Look for scale**  
  - Is the object too large or too small to be a building relative to other easily identifiable objects in the image? (It’s useful to look at what other mappers have created with the building tag in that same area.)

- **Look for patterns, shapes, and textures**  
    - Look for straight lines and rectangles, as they are most likely parts of man-made features.

- **Look for color**  
  - Large patches of grey and red are often an indication of shingled, tiled, or tin roof buildings. Also look for lines of shadow around the edges of buildings, as this indicates an elevated structure, and can be the difference between mistakenly labeling a concrete parking lot as a building.

### Distinguishing Objects

In many places, our ability to meaningfully distinguish objects from one another is limited, either due to the quality of the image or the complexity of the object on the ground. Let’s take on a few common examples, this time from Addis Ababa, Ethiopia.

![alt text](Module3_Static/3.9.png)

We can take advantage of a few things to help us trace our building footprints correctly. 

1. Shadows imply that an object is above the ground (so a roof is not a parking lot). 
2. Shadows give us a clear edge along which to trace the outside of a building. 
3. We can use multiple sources of imagery to help us decide what a specific object is and where its boundaries lie. Below is a best-guess interpretation of two buildings.

![alt text](Module3_Static/3.10a.png)

Although these buildings are reasonably distinguishable, there are a number of challenges. Shadows only provide clarity along some building edges (use other imagery). Trees hide corners or sometimes even entire objects. Finally, sometimes, imagery is just of too poor quality (grainy or cloud-ridden) to delineate an object with any degree of confidence.

![alt text](Module3_Static/3.11.png)

For instance, the green arrow points to an area that could be a building, parking lot, or construction site. Moreover, the shadows along its edges appear to come from the adjacent buildings with red and blue arrows. Looking at the red arrow building, we can see a clear line delineating both sides of the tin roof, which is a strong clue that this truly is a building. There might even be a small building along the top edge of the property marked with a yellow arrow. In this case, I would likely trace the buildings covered by the red and blue arrows and leave the yellow and green objects until either more clear imagery is available or I had the ability to see the site in person.

Looking more closely at the building under the blue arrow, we can turn to the shadows to help guide us. Below, we circled the shadows along the top edges of the building. Notice how these subtle clues can help us delineate buildings even in low-quality images.

![alt text](Module3_Static/3.12.png)

Unfortunately, tracing can get even harder in areas with complex arrangements of buildings. Looking at the buildings below, it is hard to figure out where one starts and where the other one ends, or if it is a building at all. 

![alt text](Module3_Static/3.13.png)

Clues that we are looking at buildings:
1. Scale relative to cars and trees
2. Color and orientation of flat roof panels
3. Clear shadows to the north of the roof line

OK, it’s a building, but where does it start and end? Complex structures like this are common, and it’s important that everyone knows how to deal with them. The general advice is to treat complex arrangements of buildings as a single building. It is generally better to map those features we are 99% percent sure of, rather than guessing. For instance, in the image above, we would likely create one large polygon for the southernmost structure, as follows:

![alt text](Module3_Static/3.14.png)

It is good practice, however, to check with people experienced in mapping in this area or with organizations that are likely to use this data, as their advice might depend on the objectives of the project you are working on.

```{tip} 
YouthMappers Blogspot: A Silver Lining

[A Silver Lining](https://www.youthmappers.org/post/2019/12/17/a-silver-lining) by Lila Rodriguez 

In this blog post, Lila discusses her experiences contributing to a mapping project related to mining in Ghana. Having never travelled to the mapping site, she explained how important contextual cultural knowledge is to one’s ability to interpret aerial imagery, and gain a more holistic understanding of how the landscape is modified by humans

```

### Quick Tips
Here are a few tips to help you get accustomed to working with imagery:

![alt text](Module3_Static/quicktips.png)

## Want to dig a little deeper?
Refer to the information below to learn more about imagery interpretation.

- **Image Interpretation:** [These tips](https://earthobservatory.nasa.gov/features/ColorImage) come from the NASA Earth Observatory’s writers and visualizers, who interpret images daily. These tips will help you get oriented to pull valuable information out of satellite images.

- **ReliefWeb Image interpretation:** Click [here](https://reliefweb.int/report/world/imagery-interpretation-guide-assessing-wind-disaster-damage-structures) to learn more.

- **Remote Sensing Tutorials:** Click [here](https://natural-resources.canada.ca/science-data/science-research/geomatics/remote-sensing/tutorial-fundamentals-remote-sensing) to learn more.

- **World View:** Click [here](https://worldview.earthdata.nasa.gov/) to see the most recent free satellite imagery.

## Conclusion 

### YouthMappers Academy: Skills, Proficiencies, and Standards

The following competencies derived from both the Geospatial Technology Competency Model and the National Geographic Standards are central to the successful completion of YouthMappers Academy Course: Imagery Interpretation. 

### The Geospatial Technology Competency Model:

1. Interpersonal Skills: Demonstrating the ability to work effectively with others through interaction with peers and course moderators

2. Initiative: Demonstrating gumption at work/school

3. Dependability and Reliability: Displaying responsible behaviors at work/school

4. Lifelong Learning: Displaying a willingness to learn and apply new knowledge and skills

5. Reading: Understanding written sentences and paragraphs in work-related documents 

6. Geography: Understanding the science of place and space; geographic skills

7. Basic Computer Skills: Using a computer and related applications to input and retrieve information; navigation and file management, and internet and email

8. Planning and Organizing: Planning and prioritizing work to manage time effectively and accomplish assigned tasks; planning and organizing; adaptability and flexibility; time management

9. Data Quality: Accuracy, resolution, precision, fitness for use; quality control versus quality assurance; data quality implications of legacy systems

10. Remote sensing and photogrammetry: Basic introduction

11. Geographic Information Systems: Conceptual foundations, including representation and uncertainty

### The National Geographic Standards:

1. The World in Spatial Terms: 
  - How to use maps and other geographic representations, geospatial technologies, and spatial thinking to understand and communicate information
  - How to analyze the spatial organization of people, places, and environments on Earth's surface

2. Places and Regions: 
  - The physical and human characteristics of places

3. Human Systems: 
  - The processes, patterns, and functions of human settlement
  - Human Systems: How the forces of cooperation and conflict among people influence the division and control of Earth's surface

4. Environment and Society: 
  - How human actions modify the physical environment
  - How physical systems affect human systems

5. The Uses of Geography: 
- How to apply geography to interpret the past
- How to apply geography to interpret the present and plan for the future


<div style="background-color:#91ccca;padding: 15px 30px;border-radius: 8px;">
<h3>Knowledge Checks</h3>
<p>To test your knowledge, complete the following test:</p>
<p><a href="https://forms.gle/EgfqTaNaogcQqVUp9" style="background-color: #e74c3c; color: white; padding: 10px 10px; text-decoration: none; border-radius: 8px; font-weight: bold; display: inline-block; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">🎯 Start Imagery Interpretation Quiz </a></p>
<p>If you receive a score of 80% or higher, you will receive an email with a certificate for this module.</p>
</div>

<!-- 
## Congratulations!

Congratulations on completing Course 3: Imagery Interpretation of the YouthMappers Academy series! 

![alt text](Module3_Static/badge3.gif) -->
