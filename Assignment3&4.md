---
title: Assignment3&4
layout: template
filename: Assignment3&4.md
---
## Assignment 3 & 4

### Name: Kshitij Dhara
### Andrew ID: kdhara


## Part 1: Original Data Visualization

Link to the Original Visualization: [MakeoverMonday Data Visualization](https://data.world/makeovermonday/generative-ai-search-trends-in-the-united-states)

Why I Selected This Visualization:

I chose this particular data visualization because it represents an important public dataset created by a professional organization/government agency, but I believe its clarity and presentation could be improved for better understanding. The visualization displays key data, but its color choices, layout, and comparison techniques seem to fall short in guiding the audience to gain meaningful insights efficiently.
![Original Visualization](<dataviz img/AI trends OG chart.png>)

## Part2: Critique of the Data Visualization

For the critique, I used Stephen Few's Data Visualization Effectiveness Profile as the primary evaluation tool. Here's a detailed breakdown:

Clarity: The data has regional labels hence the use of a geographpical map is logical which I like but what I don't is that it does not show the ratio to which the most used AI model compares to the other two.
Precision: The use of stacked bar charts makes it difficult to compare values across regions. Precision scored a 4 since it's hard to interpret the differences between subregions accurately.
Engagement: The visualization is static and lacks interactivity, so engagement was rated 3. Adding dynamic elements would allow users to better explore the data.
Summary of Critique Insights:
Strengths: The data visualization is well-sourced and structured, making it clear what the subject is.
Weaknesses: The poor use of colors and chart types makes it harder to compare across different categories and regions.
Overall, the Few Method helped me uncover areas of improvement but didn’t cover important aspects like interactivity.
Comparison to Good Charts Method:
Compared to Good Charts, Few's method is more focused on granular critiques like precision, while Good Charts emphasizes overall visual appeal and impact. Good Charts encourages creativity, but Few's method is more precise for evaluating each aspect of visualization.
Link to Stephen Few's Google Spreadsheet (Google Form responses): [Insert link]

## Part 3: Redesign Sketches

I created a wireframe of my initial redesign ideas. The focus was on:

Changing the chart type: Replacing the geographical map with grouped bar chart or small multiples for better comparison.
Improving color contrast: Introducing a new color scheme for better differentiation between categories.
Adding interactivity: Users can click or hover over regions to see detailed breakdowns.

<div class='tableauPlaceholder' id='viz1726693746021' style='position: relative'><noscript><a href='#'><img
                alt='Assignment 3&amp;4 temp '
                src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Tw&#47;TwD-Assignment34&#47;Sheet2&#47;1_rss.png'
                style='border: none' /></a></noscript><object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='TwD-Assignment34&#47;Sheet2' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image'
            value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Tw&#47;TwD-Assignment34&#47;Sheet2&#47;1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
        <param name='filter' value='publish=yes' />
    </object></div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1726693746021');
    var vizElement = divElement.getElementsByTagName('object')[0];
    vizElement.style.width = '100%';
    vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>


## Part 4: Testing the Redesign

User Feedback:
I shared my redesign with two different individuals:

Student, mid-20s:
Feedback: Found the grouped bar chart much easier to interpret than the original stacked chart. However, they found the use of lighter colors confusing.
Changes: Based on this feedback, I adjusted the color intensity for clearer visual differences.
Adult, late 50s:
Feedback: They struggled to identify the regions without labels. They also suggested adding more context to the visualization.
Changes: I added state labels and a small legend to provide better context for each region.
Feedback Summary:
Common Themes: Both participants appreciated the change in chart type but asked for better labeling and clearer colors.
Design Changes: I improved color contrast and added more descriptive labels, making the visualization easier to follow without an explanation.

## Part 5: Final Data Visualization

After gathering feedback, I implemented the following changes:

- Stacked bars instead of Grouped bar chart for more straightforward comparison.
- Improved color scheme with better contrast.
- State labels added to the map for easier identification.
- Hover-over interactivity introduced for additional insights without cluttering the main view.

Final Visualization:
<div class='tableauPlaceholder' id='viz1726693931586' style='position: relative'><noscript><a href='#'><img
                alt='Sheet 1 '
                src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Tw&#47;TwD-Assignment34&#47;Sheet1&#47;1_rss.png'
                style='border: none' /></a></noscript><object class='tableauViz' style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' />
        <param name='site_root' value='' />
        <param name='name' value='TwD-Assignment34&#47;Sheet1' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image'
            value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Tw&#47;TwD-Assignment34&#47;Sheet1&#47;1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
        <param name='filter' value='publish=yes' />
    </object></div>
<script type='text/javascript'>
    var divElement = document.getElementById('viz1726693931586');
    var vizElement = divElement.getElementsByTagName('object')[0];
    vizElement.style.width = '100%';
    vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>
## Conclusion:
The redesigned data visualization aims to improve clarity, comparability, and engagement. By addressing the weaknesses identified in the critique, the final product allows users to extract more meaningful insights at a glance while providing a more interactive experience. The redesign process taught me how important it is to test visualizations with real users, and I will continue applying these principles in future visualizations.