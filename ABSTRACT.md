The authors present **A Semantically Annotated 15-Class Ground Truth Dataset for Substation Equipment** with 1660 images annotated with 15 classes, including *insulators*, *disconnect_switches*, *transformers* and other equipment commonly found in substation environments. The images were captured using a combination of human, fixed and AGV-mounted cameras at different times of the day, providing a diverse set of training and testing data for algorithm development. In total, 50,705 annotations were created by a team of experienced annotators, using a standardized process to ensure accuracy across the dataset. The resulting dataset provides a valuable resource for researchers and practitioners working in the fields of substation automation, substation monitoring and computer vision. Its availability has the potential to advance the state of the art in this important area.

Table 1 provides an overview of the distribution of the images based on source. The unspecified smartphone and digital cameras collected by humans on the field are referred to as miscellaneous. The images in the dataset come in a variety of resolutions, as shown in Table 2.

|           Source              |    Camera   | Quantity |
|-------------------------------|-------------|----------|
| Human (Morning)               | Misc, T540  |	682      |
| AGV (Morning and afternoon)   | A700	      | 230      |
| AGV (Night, light)            | A700	      | 360      |
| AGV (Night, no light)	        | A700        |	348      |
| Fixed (Morning and afternoon) | A700        |	32       |
| Fixed (Night, light)          | A700        |	8        |

<span style="font-size: smaller; font-style: italic;">Table 1. Dataset distribution based on source.</span>


| Resolution  | Occurrences |
|-------------|-------------|
| 1280 × 960  | 887         |
| 2592 × 1944 | 268         |
| 2880 × 2160 | 266         | 
| 4032 × 3024 | 98          |
| 4000 × 3000 | 36          |
| 640 × 480   | 31          |
| 4624 × 3468 | 28          |
| 2048 × 1536 | 27          |
| 704 × 480   | 10          |
| 1156 × 867  | 4           |
| 1280 × 720  | 2           |
| 2324 × 1440 | 1           |
| 4624 × 2604 | 1           |
| 4672 × 3504 | 1           |

<span style="font-size: smaller; font-style: italic;">Table 2. Resolutions and occurrences of the 1660 images in this dataset.</span>


There are 15 classes of substation equipment. Table 3 lists them, along with how many times each object appears in the “Instances” column. An example of each object class is presented in Figure 1.

|              Class              | Instances  |       RGB       |
|---------------------------------|------------|-----------------|
| Background                      | -          | (000, 000, 000) |
| Open blade disconnect switch    | 310	       | (162, 000, 255) |
| Closed blade disconnect switch  | 5243	   | (097, 016, 162) |
| Open tandem disconnect switch   | 1599       | (081, 162, 000) |
| Closed tandem disconnect switch | 966        | (048, 097, 165) |
| Breaker                         | 980        | (121, 121, 121) |
| Fuse disconnect switch          | 355        | (255, 097, 178) |
| Glass disc insulator            | 3185       | (154, 032, 121) |
| Porcelain pin insulator         | 26,499     | (255, 255, 125) |
| Muffle                          | 1354       | (162, 243, 162) |
| Lightning arrester              | 1976       | (143, 211, 255) |
| Recloser                        | 2331       | (040, 000, 186) |
| Power transformer               | 768        | (255, 182, 000) |
| Current transformer             | 2136       | (138, 138, 000) |
| Potential transformer           | 654        | (162, 048, 000) |
| Tripolar disconnect switch      | 2349       | (162, 000, 096) |

<span style="font-size: smaller; font-style: italic;">Table 3. Object classes, number of instances in the dataset and their colours in RGB values used for the .png segmentation masks.</span>


![Fig 1](https://i.ibb.co/PtNnCVp/data-08-00118-g001.png)

<span style="font-size: smaller; font-style: italic;">Figure 1. An example for each of the 15 classes present in the dataset. (a) Open blade disconnect switch. (b) Closed blade disconnect switch. (c) Open tandem disconnect switch. (d) Closed tandem disconnect switch. (e) Breaker. (f) Fuse disconnect switch. (g) Glass disc insulator. (h) Porcelain pin insulator. (i) Muffle. (j) Lightning arrester. (k) Recloser. (l) Power transformer. (m) Current transformer. (n) Potential transformer. (o) Tripolar disconnect switch.</span>

The images in this dataset were captured from a single electrical distribution substation in Brazil over a period of two years, at different times of day and under varying weather and seasonal conditions, ensuring a diverse range of lighting conditions for the depicted objects. All the images underwent a curation process by experts in Electrical Engineering to ensure that the angles and distances depicted in the images were suitable for automating inspections in a substation.

According to the provided information from the electrical company overseeing the substation, the energy consumption profile exhibits a consistent pattern throughout the year. The profile shows a global minimum at 6h00, a local maximum at 13h00, a local minimum at 17h00 and a global maximum at 20h00, with slight amplitude variations. Based on this insight, a collection schedule was devised for automated inspections, encompassing time slots at 8h00, 13h00, 17h00 and 20h00. Human-led collections were conducted exclusively during the morning period to align with the availability of on-field company technicians assisting our researchers.

The human-collected images were captured by various individuals using different camera models, including smartphone cameras, unspecified digital cameras and the FLIR T540, as shown in Figure 3. There was no standardization in terms of camera angles or distances, although the maximum distance for image capture was limited to 30 m. Those images were taken during the morning period, with the time of capture ranging from 8h00 to 12h00.

![Fig.3](https://i.ibb.co/T20GB1F/data-08-00118-g003.webp)

<span style="font-size: smaller; font-style: italic;">Figure 3. A technician capturing images using the FLIR T540 camera.</span>


The Autonomous Ground Vehicle (AGV) shown in Figure 4 used the FLIR A700 camera to collect the majority of the images in this dataset. This AGV followed a predetermined path through 60 possible scenes, capturing images at fixed angles and distances ranging from 3 to 5 m. Those collections were conducted three times per day, with the specific times being in the morning (between 8h00 and 10h00), in the afternoon (between 13h00 and 17h00) and at night (between 20h00 and 21h00).

![Fig.4](https://i.ibb.co/zGyNCC4/data-08-00118-g004.webp)

<span style="font-size: smaller; font-style: italic;">Figure 4. A photo of our AGV equipped with the FLIR A700 (marked with the red box) and the FLIR A310 (the white one, with two separate lenses) cameras on a substation floor. The A310 was not used to take any photos for this dataset but was used for pan-tilt purposes for other mounted cameras.</span>

The FLIR A700 camera fixed in the substation, shown in Figure 5, collected photos also three times per day: in the morning (between 6h00 and 11h00), in the afternoon (between 13h00 and 18h00) and at night (between 21h00 and 00h00).

![Fig.5](https://i.ibb.co/9qN1bqH/data-08-00118-g005.png)

<span style="font-size: smaller; font-style: italic;">Figure 5. Photos of the A700 fixed in the substation. The camera is encircled in red in both subimages. (a) Front view of the A700. (b) Back view of the A700 showing objects in its field of view.</span>


Authors annotated the semantic dataset using the software [LabelMe](https://www.mdpi.com/2306-5729/8/7/118#B13-data-08-00118), as shown in Figure 6. The annotation process took approximately 1100 man-hours over the course of 4 months by 9 people.

![Fig.6](https://i.ibb.co/cLHtZPc/data-08-00118-g006.png)

<span style="font-size: smaller; font-style: italic;">Figure 6. Examples of manual annotation for semantic segmentation using LabelMe. The colors used by LabelMe have no relation to the colors used in the masks from Table 3. (a) Insulators (red) and breakers (green). (b) A recloser (purple).</span>


<i> Please note that DatasetNinja upload Instance version of Substation Equipment. The dataset contains objects separated by objects located in the foreground, which can lead to incorrect interpretation of data. </i>
