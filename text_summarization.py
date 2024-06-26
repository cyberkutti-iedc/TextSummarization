# -*- coding: utf-8 -*-
"""Text_Summarization.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1UrO3R8Cg_4CVyCQMzTHjLSF5UAqWXeXY
"""

!pip install transformers

from transformers import pipeline

summarizer = pipeline("summarization")

ARTICLE = """
Apple Inc., founded by Steve Jobs, Steve Wozniak, and Ronald Wayne in 1976, has emerged as one of the most influential technology companies globally, renowned for its innovation and design excellence. From its humble beginnings in a garage to becoming a trillion-dollar enterprise, Apple has redefined numerous industries through its groundbreaking technology products.

At the core of Apple's success lies its relentless focus on user experience. The company's products, including the iPhone, iPad, Macintosh computers, Apple Watch, and various software services, are meticulously designed to seamlessly integrate hardware and software, offering users intuitive and enjoyable experiences. This integration is exemplified by the iOS and macOS ecosystems, where devices work seamlessly together, fostering user loyalty and engagement.

The iPhone, introduced in 2007, revolutionized the mobile industry, setting new standards for smartphones. Its sleek design, coupled with the innovative multitouch interface, completely transformed how people interacted with their phones. With subsequent iterations, Apple continuously pushed the boundaries of performance, camera technology, and software capabilities, maintaining its position as a market leader.

In addition to hardware, Apple's software ecosystem is equally remarkable. iOS, iPadOS, macOS, watchOS, and tvOS provide cohesive experiences across various devices, ensuring consistency and ease of use for consumers. The company's commitment to privacy and security is evident in its stringent measures to safeguard user data, setting it apart from competitors and earning trust among users.

Apple's innovation extends beyond consumer electronics into services such as iCloud, Apple Music, Apple TV+, and Apple Arcade. These offerings complement its hardware lineup, providing users with seamless access to content and enhancing the overall ecosystem. The subscription-based model adopted by Apple for many of its services has proven highly successful, contributing significantly to the company's recurring revenue stream.

The Macintosh lineup has been a cornerstone of Apple's business since its inception. Renowned for their reliability, performance, and design aesthetics, Mac computers are favored by professionals and creative individuals worldwide. The transition to Apple Silicon, utilizing custom-designed chips like the M1, marks a significant milestone, further enhancing the performance and efficiency of Mac devices.

Apple's commitment to sustainability and environmental responsibility is evident throughout its operations. The company has made substantial investments in renewable energy, reduced carbon emissions, and implemented recycling programs to minimize its environmental footprint. Initiatives like the Apple Trade-In program encourage customers to recycle their old devices responsibly, furthering Apple's commitment to sustainability.

Beyond hardware and software, Apple's influence extends into emerging technologies such as augmented reality (AR) and artificial intelligence (AI). ARKit, Apple's AR development platform, empowers developers to create immersive AR experiences across iOS devices, while Siri, Apple's virtual assistant, leverages AI to provide personalized assistance to users.

The company's retail presence, characterized by its iconic Apple Stores, plays a crucial role in enhancing the overall customer experience. These stores serve as more than mere retail outlets, functioning as community hubs where customers can receive technical support, attend workshops, and engage with Apple's products firsthand.

Apple's success is not without its challenges and controversies. Antitrust scrutiny, particularly regarding the App Store's policies and fees, has drawn criticism from regulators and developers alike. Moreover, concerns surrounding labor practices in Apple's supply chain and its approach to addressing issues like e-waste and product repairability have sparked debates about corporate responsibility.

Looking ahead, Apple continues to push the boundaries of innovation, with developments in areas such as augmented reality, wearable technology, and autonomous vehicles. The company's ability to anticipate and adapt to evolving consumer needs while maintaining its commitment to quality and user experience will undoubtedly shape its trajectory in the years to come. As Apple navigates the complexities of the digital age, its legacy of innovation and its impact on technology and society are bound to endure.
"""

summarizer(ARTICLE, max_length=130, min_length=30, do_sample=False)