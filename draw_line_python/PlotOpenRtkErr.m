clear


% dif = load('C:\Users\da\Documents\317\float_test\rov_3170011--COM14_191113_003724_gga.dif');
% dif = load('C:\Users\da\Documents\322\2\2019-11-17-18-17-27--COM156_191118_021550_gga.dif');
% dif = load('C:\Users\da\Documents\322\static\2019-11-18-8-52-44--sf04_ref.dif');
% dif = load('C:\Users\da\Documents\322\static2\2019-11-18-11-29-30--sf04_ref.dif');
% dif = load('C:\Users\da\Documents\322\5\2019-11-18-09-23-41--COM156_191118_172313_gga.dif');
% dif = load('C:\Users\da\Documents\322\9\2019-11-18-14-42-54--COM156_191118_224440_gga.dif');
% dif = load('C:\Users\da\Documents\323\5\2019-11-19-17-48-21--COM131_191120_014527_gga.dif');
% dif = load('C:\Users\da\Documents\323\5\2019-11-19-17-48-21--novatel_CPT7-2019_11_19_17_46_06.dif');
dif = load('C:\Users\da\Documents\329\1\2019-11-25-18-34-03--novatel_CPT7-2019_11_25_18_29_34.dif');

idx = 1:1:length(dif);

% figure
% plot(dif(idx,1), dif(idx, 5:7), '.-')
% mean(dif(idx, 5:7))
% std(dif(idx, 5:7))

n = dif(idx, 5);
e = dif(idx, 6);

x = sqrt(n.^2 + e.^2);

dataset_tag = 'OpenRTK330LI';

%%
    hf = figure; 
    [h1, stat1] = cdfplot(x);
    % legend(gca, 'rtklib')
    
    h1.Color = [0 0.5 0];
    h1.LineWidth = 2;
    hold on
    % figure
%     [h2, stat2] = cdfplot(abs(sol_spp(idx_spp,hor_col)));
%     h2.Color = 'r'; h2.LineWidth = 1.5;
    % legend(gca, 'openrtk')
    % figure;
    % [h3, stat3] = cdfplot(abs(sol_rtklib(:,hor_col)));

    % xlim(gca, [0 2]);
    xlabel(gca, 'Horizontal error (m)')
    ylabel(gca, 'CDF')
%     legend(gca, {'new', 'old'})
    title(gca, ['Aceinna ', dataset_tag]);
%     savefig(hf, [subf1, dataset_tag{1}, res_key]);

%% CEP bar plot
if 0
    RMS2CEP = 1.2;
    Y = prctile(abs(sol(idx, 8)), [50, 68, 95, 99], 1)./RMS2CEP;
    
%     Yspp = prctile(abs(sol_spp(idx_spp, 8)), [50, 68, 95, 99], 1)./RMS2CEP;
    
    hbg = figure;
    bh = bar([Y, Yspp]);  grid on
    ylabel(gca, 'Horizontal error (m)');
    ax = gca;
    ax.XTickLabel = {'CEP50', 'CEP68', 'CEP95', 'CEP99'};
    set(bh(1), 'FaceColor', [0, 0.5, 0])
    set(bh(2), 'FaceColor', 'r')
%     legend(gca, {'new', 'old'})
    title(gca, ['Aceinna ', dataset_tag]);
%     savefig(hbg, [subf1, dataset_tag{1}, '-cep']);
end
%%
%     figure; hold on
%     plot(sol(idx, 1), sol(idx, 8), 'Color', [0, 0.5, 0]);
%     plot(sol_spp(idx_spp, 1), sol_spp(idx_spp, 8), 'r.-');