**先验概率、后验概率、似然函数、贝叶斯定理**

[(128条消息) 一个例子搞清楚（先验分布/后验分布/似然估计）_本帅哥屏蔽了凡人的博客-CSDN博客](https://icaoys.blog.csdn.net/article/details/78265026?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-1-78265026-blog-120000864.235%5Ev28%5Epc_relevant_multi_platform_whitelistv3&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7ERate-1-78265026-blog-120000864.235%5Ev28%5Epc_relevant_multi_platform_whitelistv3&utm_relevant_index=1)



隔壁王大爷去15公里外的一个公园，可能的交通方式有步行，骑车，开车。当他花了一个小时，很大可能是骑车过去的，也有可能是堵车堵了很久，极小可能是大爷走路过去的；花了三个小时，很大可能是走路过去的；花了20分钟，很大可能是开车过去的。 

**三个概念之后验（知果求因）**

这种预先**已知结果**（路上花的时间），然后根据结果**估计**（猜）**原因**（交通方式）的概率分布即 **后验概率**(后验分布)。$P(因|果)$  $P(\theta|x)$



 **三个概念之先验概率（由历史求因）**

假如王大爷喜欢运动，走路过去的概率最大。在**结果发生前**就开始猜测原因（交通方式）

根据历史规律确定**原因** （交通方式）的概率分布即 **先验概率**（先验分布)。 $P(因)$  $P(\theta)$



**三个概念之似然估计（由因求果）**

假如先知道王大爷的交通方式，比如步行去，一般大概要3个小时，当然可能大爷跑步过去的，花了一个多小时；假如大爷决定开车去，非常可能半个小时内到公园，非常小的概率堵车花了3个小时。

这种**先定下来原因**，**根据原因来估计结果**的概率分布即 **似然估计**。根据原因来统计各种可能结果的概率即**似然函数**。 $P(果|因)$ $P(x|\theta)$



贝叶斯公式

$P(\theta|x)=\frac{P(x|\theta)∗P(\theta)}{P(x)}​$  $P(A|B)=\frac{P(B|A)*P(A)}{P(B)}$

$P(x)$即evidence，只统计每次到达公园的时间$x$

最大似然估计（极大似然估计）（MLE，Maximum Likelihood）

$argmax_\theta P(x|\theta)$

最大后验估计（MAP－Maxaposterior）

$argmax_\theta ​P(\theta|x)=argmax​_\theta \frac{P(x|\theta)∗P(\theta)}{P(x)}​$

[(133条消息) 详解最大似然估计（MLE）、最大后验概率估计（MAP），以及贝叶斯公式的理解_均匀分布的mle_耐耐~的博客-CSDN博客](https://blog.csdn.net/f156207495/article/details/104671972/)



**变分自动编码器**

没有太多的推理过程

[机器学习方法—优雅的模型（一）：变分自编码器（VAE） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/348498294?utm_id=0)

[变分自编码器（一）：原来是这么一回事 - 科学空间|Scientific Spaces](https://spaces.ac.cn/archives/5253)

已知人的外貌x，求其特征z(身高，肤色)  这就是后验分布$p(z|x)$  通过Encoder，学习$q(z|x)$ 来近似$p(z|x)$

已知特征，生成人的外貌，

$KL(N(\mu,\sigma^2)||N(0,1)) = \frac{1}{2}(-log \sigma^2+\mu^2+\sigma^2-1)$

正态分布二阶矩 $\mu^2+\sigma^2$

[一起啃PRML - 1.2.4 The Gaussian distribution 高斯分布 正态分布 - AI_Believer - 博客园 (cnblogs.com)](https://www.cnblogs.com/chxer/p/5351734.html)

变分推断

[Bayesian inference problem, MCMC and variational inference | by Joseph Rocca | Towards Data Science](https://towardsdatascience.com/bayesian-inference-problem-mcmc-and-variational-inference-25a8aa9bce29)

[【学习笔记】生成模型——变分自编码器 (gwylab.com)](https://www.gwylab.com/note-vae.html)
