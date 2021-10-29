function [t,v1,v2] = get_rigol_csv(filename,varargin); 
% function [t,v1,v2] = get_rigol_csv(filename,varargin)
% 
% estrarre dati (t, v1, v2) da un file filename.csv generato dall'oscilloscopio 
% Rigol MS02102A
% opzione 'no_talk' spegne report a video
%
% wjwiv 20201020

talk = true; 

if length(varargin)>0
    for jj=1:length(varargin)
        if strcmp(varargin{jj},'no_talk')
            talk = false;
        end
    end
end

dat = csvread([filename '.csv'],2);
tdat = csvread([filename '.csv'],1,3,[1, 3, 1, 4]);

if talk
    disp([' File ' filename '.csv, ' int2str(size(dat,1)) ' punti con ' ... 
        int2str(size(dat,2)) ' colonne']);
end
toff = tdat(1); DT = tdat(2);
t = dat(:,1)*DT + toff;
v1 = dat(:,2);
if size(dat,2)>2
    v2 = dat(:,3);
else
    v2 = []; 
end
