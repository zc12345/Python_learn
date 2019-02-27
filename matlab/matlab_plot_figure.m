clear;clc;
all_ = 9;
col = 3;
row = 3;
imgdir = '../keypoint_detection/data/val/image/';
preddir = '../keypoint_detection/data/val/prediction-v5-10pts/';
outdir = '../keypoint_detection/data/val/out_plot_10/';

%% 1. add mask
% Display the keypoints

img_args = struct2cell(dir([imgdir,'*.jpg']));
img_fns = img_args(1,:);
all_ = numel(img_fns);

for i = 1:all_
    
fn = char(img_fns(i));
fn = fn(1:end-4);
img_fn = sprintf('%s%s.jpg', imgdir, fn);
pred_fn = sprintf('%s%s-10point.txt', preddir, fn);
out_fn = sprintf('%sroad_fig_%d.png',outdir, i);

img = imread(img_fn);
[kpx, kpy] = textread(pred_fn, '%d%d');
% % process pts
% [kpx1, kpy1] = gen_line(kpx(1:end/2), kpy(1:end/2));
% [kpx2, kpy2] = gen_line(kpx(end/2+1:end), kpy(end/2+1:end));
% s = 5;
% n1 = numel(kpx1);
% n2 = numel(kpx2);
% p1 = floor(n1/s);
% p2 = floor(n2/s);
% m1 = mod(n1, s);
% m2 = mod(n2, s);
% for i = 1:s
%     kpx11(i) = kpx1(m1+p1*i);
%     kpy11(i) = kpy1(m1+p1*i);
%     kpx21(i) = kpx2(p2*(i-1) + 1);
%     kpy21(i) = kpy2(p2*(i-1) + 1);
% end
% kpx = [kpx11 kpx21];
% kpy = [kpy11 kpy21];
% adjust some keypoint coordinates
lw_kpx = [0 0 kpx(1:end/2)' kpx(end/2)];lw_kpy = [0 kpy(1) kpy(1:end/2)' 0];
rw_kpx = [kpx(end/2 + 1) kpx(end/2 + 1:end)' 1280 1280];rw_kpy = [0 kpy(end/2 + 1:end)' kpy(end) 0];
bg_kpx = [kpx(end/2) kpx(end/2) kpx(end/2 + 1) kpx(end/2 + 1)];bg_kpy = [0 kpy(end/2) kpy(end/2 + 1) 0];
rp_kpx = [0 0 kpx' 1280 1280];rp_kpy = [1024 kpy(1) kpy' kpy(end) 1024];

% plot with color mask
figure(1);
imshow(img); hold on;
plot(kpx, kpy, 'r.', 'MarkerSize', round(size(img,2)/15)); hold on;
hold on;  
fill (lw_kpx,lw_kpy,'r','facealpha',0.5);
fill (rw_kpx,rw_kpy,'g','facealpha',0.5);
fill (bg_kpx,bg_kpy,'b','facealpha',0.5);
fill (rp_kpx,rp_kpy,'yellow','facealpha',0.5);
% save figure
frame=getframe(gca); 
imwrite(frame.cdata,out_fn);

end

%% 2. subplot
%{
figure(1) ; clf ;
title('detection results');
set(gcf,'Position',[0,0,1280, 1024], 'color','w');
outdir = './out_plot/';
img_args = struct2cell(dir([outdir,'*.png']));
img_fns = img_args(1,:);
for ii = 1:9
    out_fn = sprintf('%s%s',outdir, char(img_fns(ii)));
    im = imread(out_fn);
    % adjust sub figure 
    subplot('Position',[(mod(ii-1,col))/col+ 0.005,1-(ceil(ii/col))/row + 0.005,1/col-0.01,1/row-0.01]);
    imshow(im) ;
end
frame=getframe(figure(1)); 
imwrite(frame.cdata,'test_result.png');
%}
function ha = tight_subplot(Nh, Nw, gap, marg_h, marg_w)

% tight_subplot creates "subplot" axes with adjustable gaps and margins
%
% ha = tight_subplot(Nh, Nw, gap, marg_h, marg_w)
%
%   in:  Nh      number of axes in hight (vertical direction)
%        Nw      number of axes in width (horizontaldirection)
%        gap     gaps between the axes in normalized units (0...1)
%                   or [gap_h gap_w] for different gaps in height and width 
%        marg_h  margins in height in normalized units (0...1)
%                   or [lower upper] for different lower and upper margins 
%        marg_w  margins in width in normalized units (0...1)
%                   or [left right] for different left and right margins 
%
%  out:  ha     array of handles of the axes objects
%                   starting from upper left corner, going row-wise as in
%                   going row-wise as in
%
%  Example: ha = tight_subplot(3,2,[.01 .03],[.1 .01],[.01 .01])
%           for ii = 1:6; axes(ha(ii)); plot(randn(10,ii)); end
%           set(ha(1:4),'XTickLabel',''); set(ha,'YTickLabel','')

% Pekka Kumpulainen 20.6.2010   @tut.fi
% Tampere University of Technology / Automation Science and Engineering


if nargin<3; gap = .02; end
if nargin<4 || isempty(marg_h); marg_h = .05; end
if nargin<5; marg_w = .05; end

if numel(gap)==1; 
    gap = [gap gap];
end
if numel(marg_w)==1; 
    marg_w = [marg_w marg_w];
end
if numel(marg_h)==1; 
    marg_h = [marg_h marg_h];
end

axh = (1-sum(marg_h)-(Nh-1)*gap(1))/Nh; 
axw = (1-sum(marg_w)-(Nw-1)*gap(2))/Nw;

py = 1-marg_h(2)-axh; 

ha = zeros(Nh*Nw,1);
ii = 0;
for ih = 1:Nh
    px = marg_w(1);

    for ix = 1:Nw
        ii = ii+1;
        ha(ii) = axes('Units','normalized', ...
            'Position',[px py axw axh], ...
            'XTickLabel','', ...
            'YTickLabel','');
        px = px+axw+gap(2);
    end
    py = py-axh-gap(1);
end
end
